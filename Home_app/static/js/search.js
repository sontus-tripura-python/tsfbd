const searchField = document.querySelector('#searchField');
const userListTable = document.querySelector(".user-table");
const userListOuput = document.querySelector('.output-box');
const userList = document.querySelector('.user_list');
userListOuput.style.display= "none";

searchField.addEventListener("keyup",(e)=>{
   const searchValue = e.target.value;
   if(searchValue.trim().length>0){
       console.log('saerching', searchValue)
       fetch('/member/student-search/',{
           body: JSON.stringify({searchTextValue : searchValue }),
           method: "POST",
       })
       .then((res)=>res.json())
       .then((data)=>{
           console.log('data', data);
           userListTable.style.display = "none";
           userListOuput.style.display= "block";
        

           if(data.length===0){
            userListOuput.innerHTML = `<h2>No results found</h2>`;
           }else{
               data.foreach((item)=>{
                userList.innerHTML += `
             
       
                    <div class="user_profile">
                      <li>
                         
                        <a href="{% url 'view_profile' pk=user.pk %}">
                          <img src="${ item.profile.photo.url }" alt="" class="rounded-circle profilepic">
                              </a>
                   
                    <a href="{% url 'view_profile' pk=user.pk %}" class="name_link">
                    <span class="profile_name">${ item.first_name} ${ item.last_name }</span>
                    </a>
                    </li>
                    </div>
 
               
                `
               })
             

           }
       })
   }else{
    userListOuput.style.display = "none";
    userListTable.style.display = "block";
   }
});
