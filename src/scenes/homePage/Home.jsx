import React from 'react'
import Welcom from '../content/Welcom'
import Team from '../content/team'
import "./home.css"

export default function Home() {
  return (
    <div className='container'>
      <div className="left-side">
       <Welcom/>
      </div>
      <div className="right-side">
        <Team/>
      </div>
    </div>
  )
}
