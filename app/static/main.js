(function() {
    console.log('ready!'); // sanity check
  })();
  
  const postElements = document.getElementsByClassName('entry');
  
  for (var i = 0; i < postElements.length; i++) {
    postElements[i].addEventListener('click', function() {
      const postId = this.getElementsByTagName('h2')[0].getAttribute('id');
      const node = this;
      fetch(`/delete/${postId}`)
        .then(function(resp) {
          return resp.json();
        })
        .then(function(result) {
          if (result.status === 1) {
            node.parentNode.removeChild(node);
            console.log(result);
          }
          location.reload();
        })
        .catch(function(err) {
          console.log(err);
        });
    });
  }

  function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      for (j = 0; j < 5; i++) {
        td = tr[i].getElementsByTagName("td")[j];
        if (td) {
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    }
  }