function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
  
    if (sidebar.style.width === "60px") {
      sidebar.style.width = "170px";
    } else {
      sidebar.style.width = "60px";
    } 
  }
  