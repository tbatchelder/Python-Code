function hourGlassSum(arr) {
  // Container for 2D integer list
  const arr_temp = [];

  for (let i = 0; i < 6; i++) {
    temp = arr[i].split(" ").map(function (item) { return parseInt(item, 10) });
    arr_temp.push(temp);
  }
  
  // REMEMBER TO REMOVE ALL OF THE INFO ABOVE WHICH IS PARSING HTE STRING ... HACKERRANK DOES THIS FOR US.
  
  const totals = [];

  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      let total = arr_temp[i][j] + arr_temp[i][j + 1] + arr_temp[i][j + 2];
      total = total + arr_temp[i + 1][j + 1];
      total = total + arr_temp[i + 2][j] + arr_temp[i+2][j + 1] + arr_temp[i+2][j + 2];
      totals.push(total);
    }
  }
 
  return Math.max(...totals);
}

console.log(hourGlassSum(["-9 -9 -9 1 1 1", "0 -9 0 4 3 2", "-9 -9 -9 1 2 3", "0 0 8 6 6 0", "0 0 0 -2 0 0", "0 0 1 2 4 0"]))