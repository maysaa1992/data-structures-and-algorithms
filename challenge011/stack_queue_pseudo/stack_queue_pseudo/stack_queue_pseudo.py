class pseudo_queue:
    def PseudoQueue_enqueue(stack,arg):
        stack.push(arg)
        return stack   
    def PseudoQueue_dequeue(S1,S2):
        while S1.top is not None:
            S2.push(S1.top)
            S1.pop()
        S2.pop()
        while S2.top is not None:
            S1.push(S1.top)
            S2.pop()
        return S1    
                
        