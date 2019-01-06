class Stack
  @@count = 0
  @@storage = {}

  def push(value)
    @@storage[@@count] = value
    @@count = @@count + 1
  end
  def pop
    if @@count == 0
      return
    end
    @@count = @@count - 1
    @@storage.delete(@@count)
    return @@storage
  end
end

# stack = Stack.new()
# stack.push(1)
# stack.push(2)
# stack.push("Lol")
# stack.push(3)
# stack.pop()