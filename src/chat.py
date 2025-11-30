# %%
import openai
from typing import List, Callable
import json


# %%
model_priority_list=["gpt-4o-mini", "gpt-4.1-nano"]

class Chat():
    def __init__(self,
                 model: str,
                 tool_list: List = None,
                 tool_runner: Callable = None,
                 max_output_tokens:int=1000,
                 model_priority_list:List=model_priority_list,
                 system_prompt: str="You are a helpful assistant. Use tools immediately without asking when the user's request is clear. However, if for any reason you are offering me to use a tool, wait for my confirmation before proceeding",
                 num_iter_tool_max: int=10
                 ):
        self.model=model
        self.tool_list=tool_list
        self.tool_runner=tool_runner
        self.max_output_tokens=max_output_tokens
        self.model_priority_list=model_priority_list
        self.system_prompt=system_prompt
        self.num_iter_tool_max=num_iter_tool_max
        self.set_client()

    def set_new_history(self):
        self.msg_history=[]

    def set_client(self):
        self.client=openai.OpenAI()
        self.priority="priority" if self.model in self.model_priority_list else None
        self.set_new_history()

    def set_response(self):
        response=self.client.responses.create(
            model=self.model,
            service_tier=self.priority,
            instructions=self.system_prompt,
            input=self.msg_history,
            tools=self.tool_list,
            max_output_tokens=self.max_output_tokens
        )
        return response


    def run_chat(self):
        while True:
            user_input=input("\n************* User: ")
            if user_input.lower() in ["/exit", "/quit", "quit", "exit"]:
                break
            msg={
                "role": "user",
                "content": user_input
            }
            self.msg_history.append(msg)
            response=self.ask_and_log_reply()

            # process response to print it or call stuff
            self.process_response(response)

    def ask_and_log_reply(self):
        response=self.set_response()
        # Save outputs (function calls or other) for subsequent requests
        self.msg_history.extend([item.model_dump() for item in response.output])
        return response

    def print_answer(self,response):
        output_text=response.output_text #safer to use than output_text=response.output[0].content[0].text
        print(f"\n************* Robot: {output_text}")

    def scan_for_tool_calls(self, response):
        idx_tool_calls=[]
        for item_idx, item in enumerate(response.output):
            if item.type=="function_call":
                idx_tool_calls.append(item_idx)
        return idx_tool_calls

    def process_tools_for_one_response(self, response, idx_tool_calls: List):
        for item_idx in idx_tool_calls:
            item=response.output[item_idx]

            fcn_name=item.name
            call_id=item.call_id
            arguments=json.loads(item.arguments)
            result=self.tool_runner(fcn_name, arguments)
            # Provide function call results to the model
            self.msg_history.append({
                "type": "function_call_output",
                "call_id": call_id,
                "output": json.dumps(result)
            })

    def process_response(self, response):
        idx_tool_calls=self.scan_for_tool_calls(response)
        iter_tool=-1
        if len(idx_tool_calls)>0:
            for iter_tool in range(self.num_iter_tool_max):
                print(f"Tool iteration {iter_tool+1}/{self.num_iter_tool_max}")
                if iter_tool>0:
                    idx_tool_calls=self.scan_for_tool_calls(response)
                    if len(idx_tool_calls)==0:
                        # no more tool calls have been made - we can answer
                        break
                self.process_tools_for_one_response(response, idx_tool_calls)

                response=self.ask_and_log_reply()


        if len(idx_tool_calls)==0 and iter_tool==-1:
            # system never meant to call any tools
            self.print_answer(response)
        elif len(idx_tool_calls)==0 and iter_tool>=0:
            # system called tools and converged to an answer
            self.print_answer(response)
        else:
            # system is calling tools past the maximum number of allowed iterations. It failed
            print("System wasn't able to find an answer")
            self.print_answer(response)
