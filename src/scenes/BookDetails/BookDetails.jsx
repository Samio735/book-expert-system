import React from 'react'
import { Link } from 'react-router-dom';
import PersonalInfo from '../../componant/PersonalInfo'
import Search from '../../componant/Search'
import Button from '../../componant/Button'
import downloading from "../images/icons8-downloading-updates-100 1.png"
import connect from "../images/icons8-connect-128 1.png"
import save from '../images/icons8-bookmark-100 2.png'
import "./BookDetails.css"

export default function BookDetails(props) {
    // const content = props.location.state.content;

  return (
    <div className='DetailsContent'>
      <div className='Nav-Conta'>
        <Search/>
        <div className="Inf">
         <PersonalInfo/>
        </div>
      </div>

      <div className="pageElement">
        <div className="imageCO">
        
        </div>
        <div className="EContent">
            <h1>Can’t hurt me son</h1>
            <h2>David Goggins</h2>
            <p>
             Get ready to dominate your inner 
             voices and learn how to stay hard son .
             Get ready to dominate your inner voices
             and learn how to stay hard son .  
            </p>
        </div>
      </div>
      <div className="Details">
        <div className="btn-">
            <Link to={"/BookSummary"}>
             <Button props={"Read The Summary"}/>
            </Link>
            <div className='lgg'>
                <img src={save} alt="" />
                <img src={connect} alt="" />
                <img src={downloading} alt="" />
            </div>
        </div>

       <div className='' style={{margin:'3rem 1rem 2rem 4rem'}}>
        <div className="DetailsBook">
              <div className="Description">
                  <h1>Description</h1>
                  <p>
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  Start your Journey 
                  </p>
              </div>
              <div className='MoreDetails'>
                  <div className="Editors">
                      <h1>Editors</h1>
                      <p>David Goggins , Andrew Tate , Tristian Tate</p>
                  </div>
                  <div className="Language">
                      <h1>Languages</h1>
                      <p>English , Arabic , French</p>
                  </div>
              </div>
          </div>
          <hr className='line' />
          <div className="Comments">
              <h1>Comments</h1>
          </div>        
       </div>
      </div>

    </div>
  )
}
