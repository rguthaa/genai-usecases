
"""
   Not really how langchain runnable work, but the idea is similar instead it uses pipe (|)

   Examples of python closures
"""

class MyRunnable:
    def __init__(self, func):
        self.func = func

    def invoke (self, input):
        return self.func(input)
    
    def pipe (self, next_runnable):
        def pipe_fn (x):
            return next_runnable.invoke (self.invoke(x))
        return MyRunnable(pipe_fn)

formatter = MyRunnable (lambda x: f"Prompt: {x}")
llm = MyRunnable (lambda y: "Paris.")
parser = MyRunnable (lambda z: {"answer": z.strip(".")})

pipeline = formatter.pipe(llm).pipe(parser)
res = pipeline.invoke("What is the capital of France?")
print (res)
