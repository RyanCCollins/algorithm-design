# Standard insertion sort algorithm
class Array
  def insertion_sort
    (1..self.length).each_with_index do |i, index|
      element = self[index]
      position = index
      while element < self[position - 1] && position > 0
        self[position] = self[position - 1]
        self[position - 1] = element
        position -= 1
      end
    end
    self
  end
end
