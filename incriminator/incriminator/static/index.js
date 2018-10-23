new Vue({
    el: '#app',
    data: {
      ip: '',
      date: '',
      hello: ''
   },
   methods: {
     diveIn: function(e) {
       if(this.ip && this.date) {
         this.hello = "Hello world!";
         // We have a valid ip/date pair! We now proceed to
         // look up data for these values.
       }
       else {
         this.hello = "Invalid info :()";
       }
     }
   }
})
