import React from 'react'
import "./SignIn.css"
import { NavLink } from 'react-router-dom';

export default function SignIn() {
  return (
    <div className='SignPG'>
        <div className="sign-left">
            <div className='title'>
                <h1><span>M</span>y<span>R</span>ead</h1>
            </div>
            <div className="book-info">
                <div className="p1">
                    <p>
                       Digital
                    platform 
                    for online 
                    <span>
                    Book Summaries
                    </span>
                    </p>
                </div>

                <hr className="line" />
                <hr className="line" />

                <div className="p2">
                    <p>
                    You will never know everything , 
                    But you will know more
                    </p>
                </div>

                <hr className="line" />
                <hr className="line" />
            </div>
        </div>
        <div className="sign-right">
            <h1>Welcome Back !</h1>
            <p>
             The faster you fill up , the faster you get a ticket
            </p>
            <hr className="line" />
            <label htmlFor="">UserName</label>
            <input type="text" name="username" id="username" />

            <label htmlFor="">Password</label>
            <input type="password" name="password" id="password" />

            <div className='Sing-C'>
                <p>
                    Not a member yet ?
                    <br />
                    <span>join us now</span>
                </p>
                <button className='btn-SignIn'>
                    <a href='/GetStarted'>SignIn</a>
                </button>
            </div>
        </div>
    </div>
  )
}
