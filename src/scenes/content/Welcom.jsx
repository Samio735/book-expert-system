import React from 'react'
import { NavLink } from 'react-router-dom'
import "./Welcome.css"

export default function Welcom() {
  return (
    <div>
        <div className='left-side'>
            <h1>Welcome to my App</h1>
            <div className="start">
                <div>
                    <h1>start</h1>
                </div>
                <div className="content">
                    <p>
                      An expert system is a type of artificial intelligence (AI) 
                      program designed to simulate the problem-solving ability of 
                      a human expert in a particular domain or field. It is a 
                      computer-based system that uses knowledge, inference, 
                      and reasoning to solve complex problems and provide advice 
                      or recommendations to users.
                    </p>
                </div>
            </div>
            <button className='Get-started'>
              <NavLink to={"/Main"} >Get Started</NavLink>
            </button>
        </div>
    </div>

  )
}
