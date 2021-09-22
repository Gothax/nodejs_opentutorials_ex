var members = ['k','h','j'];
var i = 0;
while(i<members.length){
  console.log(`member log ${i}`, members[i]);
  i += 1;
};
console.log(members[1]);

var roles = {
  'programmer':'k',
  'designer ':'h',
  'manager':'l'
}
console.log(roles.programmer);
for(name in roles){
  console.log(name, roles[name]);
};
