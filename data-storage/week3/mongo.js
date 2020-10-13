const seconds = () => {
  let day = 24
  let week = 7

  return day * 60 * 60 * week
}

const weeks = () => {
  let years = 80
  let days = years * 365

  return days / 7
}

console.log(weeks())
