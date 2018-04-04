var x = 22;
$('#upvote').click(function(){
  this.id = 'inc';
  x=x+1;
  $('#inc').text("Upvote | "+ x)
  console.log(x);
  var y = $('#inc').text();
  console.log(y);
})
//$('#inc').click(function(){
//  x=x+1;
//  $('#inc').text("Upvote | "+ x)
//})
