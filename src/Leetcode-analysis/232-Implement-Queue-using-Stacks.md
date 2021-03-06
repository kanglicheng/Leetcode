# [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

使用栈来实现队列，首先我们得知道栈与队列的特性。栈是先进后出，相反，队列是先进先出。所以，为了实现队列，可以使用两个栈来实现，一个栈是用来接收push到队列里面的元素，另一个栈是用来pop出队列元素。当pop栈没有元素的时候，可以将push栈中的元素pop到pop栈中，这样，正好可以做到先进先出。类似的就不难想了。

	class MyQueue {
	
		private Stack<Integer> pushStack = new Stack<Integer>();
		private Stack<Integer> popStack = new Stack<Integer>();
		
		// Push element x to the back of queue.
	    public void push(int x) {
	        pushStack.push(x);
	    }

	    // Removes the element from in front of queue.
	    public void pop() {
	        if(!popStack.isEmpty()) popStack.pop();
	        else{
	        	while(!pushStack.isEmpty()){
	        		popStack.push(pushStack.pop());
	        	}
	        	if(!popStack.isEmpty()) popStack.pop();
	        }
	    }

	    // Get the front element.
	    public int peek() {
	        if(!popStack.isEmpty()) return popStack.peek();
	        else{
	        	while(!pushStack.isEmpty()){
	        		popStack.push(pushStack.pop());
	        	}
	        	return popStack.peek();
	        }
	    }

	    // Return whether the queue is empty.
	    public boolean empty() {
	        if(popStack.isEmpty() && pushStack.isEmpty()) return true;
	        else return false;
	    }
	}



