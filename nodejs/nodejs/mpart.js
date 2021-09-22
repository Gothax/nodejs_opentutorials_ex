var M = {
  v:'val',
  f:function(){
    console.log(this.v);
  }
}

module.exports = M;  //다른 디렉토리에서 사용하도록 수출
