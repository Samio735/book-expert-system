import React, { useState,useEffect } from 'react'
import axios from 'axios';
import "./GetStarted.css"

export default function GetStarted() {

  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    user_name:'',
    gender:'',
    email: '',
    password:'',
  });

  useEffect(()=>{

  },[])

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // ! Not Complete
  const submitForm = async() => {
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }
  
    let GetStartForm = new FormData();
    GetStartForm.append("first_name",formData.first_name)
    GetStartForm.append("last_name",formData.last_name)
    GetStartForm.append("email",formData.email)
    GetStartForm.append("password",formData.password)
    GetStartForm.append("password",formData.gender)
    GetStartForm.append("password",formData.user_name)
    await axios({
      method:'PUT',
      url:'http://localhost:8000/api/',
      data:formData
    }).then((Res) =>{
        console.log(Res.data)
      });
    try{

    }
    catch(error){
        console.log(error);
        alert(error)      
    }

  };
  return (
    <div className='GetStart'>
      <div className="start-left">
        <h1 className='start-title'>Get Started</h1>
        <p>Get yourself an account now</p>
        <div className='inputInfo'>
          <div className='pers-info'>
            <div>
              <label htmlFor="">First Name</label>
              <input type="text" name="" id="" onChange={handleChange}/>
            </div>

            <div>
              <label htmlFor="">Last Name</label>
              <input type="text" name="" id="" onChange={handleChange}/>  
            </div>

            <div>
              <label htmlFor="">Username</label>
              <input type="text" name="" id=""onChange={handleChange} />  
            </div>

            <div>
              <label htmlFor="">Gender</label>
              <input type="text" name="" id="" onChange={handleChange}/>
            </div>
          
          </div>

          <div className='infoEP'>
            <label htmlFor="">Email</label>
            <input type="email" name="" id="" onChange={handleChange}/>
            
            <label htmlFor="">Password</label>
            <input type="password" name="" id="" onChange={handleChange}/>

            <label htmlFor="">Confirm your password</label>
            <input type="password" name="" id="" onChange={handleChange}/>
          </div>
        </div>
        <button className='Creat-account' type='submit' onClick={submitForm}>
        create acount
        </button>
      </div>
      <div className="start-right">
        <div className='title'>
          <h1><span>M</span>y<span>R</span>ead</h1>
        </div>
        <div className='right-contant'>
          <h1>Start your journey with us</h1>
          <div className='description'>
            <p>
            Discover hundreds of book summaries save time and boost your self in any field you want
            </p>
          </div>
        </div>
        
      </div>
    </div>
  )
}
