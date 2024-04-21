import React, { useRef } from 'react'
import { NavLink } from 'react-router-dom'
import './navbar.css'

const netLink = [
    {
    display:'Home',
    url:'/'
},
{
    display:'About',
    url:'/about'
}
,
{
    display:'Contact',
    url:'/contact'
}
]

export default function Navbar() {

    const menuRef = useRef()
    return (

        <nav className='header'>
            
            <div className="navigation">
                <div className="logo">
                    <a href="index.html">
                        <svg id="logo-35" 
                            width="50" 
                            height="39" 
                            viewBox="0 0 50 39" 
                            fill="none" 
                            xmlns="http://www.w3.org/2000/svg">
                            <path d="M16.4992 2H37.5808L22.0816 24.9729H1L16.4992 2Z" 
                            class="ccompli1" fill="#007AFF"></path>
                            <path d="M17.4224 27.102L11.4192 36H33.5008L49 13.0271H32.7024L23.2064 27.102H17.4224Z" 
                            class="ccustom" 
                            fill="#312ECB"></path> 
                        </svg>
                    </a>
                </div>

                <div>
                    <div className="nav_menu" ref={menuRef}>
                        <ul className="nav_list">
                            {
                                netLink.map((item,index)=>(
                                    <li className="nav_item" key={index} >
                                        <NavLink to={item.url}>{item.display}</NavLink>
                                    </li>
                                ))   
                            }                      
                        </ul>
                    </div>
                </div>
                <div>
                    <button className="login">
                        Login
                    </button>
                    <button className= "GetStarted">
                        Get Started
                    </button>
                </div>
            </div>
            

        </nav>
    )
}
