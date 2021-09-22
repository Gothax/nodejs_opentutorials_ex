var fs = require('fs');

//readFileSync
console.log('A');
var result = fs.readFileSync('syntax/sample.txt','utf8');
console.log(result);
console.log('C');

console.log('A');
fs.readFile('syntax/sample.txt','utf8',function(err,result){
  console.log(result);
}); //readfile은 3번째 인자로 함수를 줘야한다 읽고 - error 면 인자로 err / err없으면 파일의 내용을 인자로 공급
console.log('C');
