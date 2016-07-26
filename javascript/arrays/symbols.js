const myObj = {
  [Symbol('Mark')]: {
    grade: 50,
    gender: 'Male',
  },
  [Symbol('Olivia')]: {
    grade: 80,
    gender: 'Female'
  },
  [Symbol('Olivia')]: {
    grade: 80
  }
}

// To get an array of iterables from a list of values with symbol keys:
const syms = Object.getOwnPropertySymbols(myObj)
const data = syms.map(i => myObj[i])
