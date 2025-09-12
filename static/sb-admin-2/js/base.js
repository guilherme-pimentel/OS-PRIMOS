document.addEventListener('DOMContentLoaded', function() {
      const userMenu = document.getElementById('userMenu');
      const userDropdown = document.getElementById('userDropdown');
      
      
      userMenu.addEventListener('click', function(e) {
        e.stopPropagation();
        userDropdown.classList.toggle('show');
      });
      
     
      document.addEventListener('click', function(e) {
        if (!userMenu.contains(e.target)) {
          userDropdown.classList.remove('show');
        }
      });
    });
