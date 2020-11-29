  // window.onload = function () {
  //       var additional_info = document.getElementById('additional_info');
  //       additional_info.style.display='none';
  //       console.log('test')
  //     };
 document.addEventListener("DOMContentLoaded", () => {
     var region = document.getElementById('id_region');
     var status = document.getElementById('id_status');
     regionChanged(region);
     hideAdditionalInfo(status);
  });

      function regionChanged(obj) {
          var district = document.getElementById('district');
          var city = document.getElementById('city');
          if (obj.value === '1') {
              district.style.display = 'block';
              city.style.display = 'none';
          } else {
              city.style.display = 'block';
              district.style.display = 'none';
          }
      }

      function hideAdditionalInfo(obj) {
          var additional_info = document.getElementById('additional_info');
          if (obj.value === '1') {
              additional_info.style.display = 'block';

          } else {
              additional_info.style.display = 'none';
          }
      }