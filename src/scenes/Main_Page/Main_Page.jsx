import React from 'react'
import { useNavigate,Link } from 'react-router-dom';
import PersonalInfo from '../../componant/PersonalInfo'
import Search from '../../componant/Search'
import "./Main_Page.css"
import Button from './../../componant/Button';

const BookList = [
    {
    image:'',
    title:'Fire and Shitty crap in asd teq'
  },  {
    image:'',
    title:'Fire and Shitty crap in asd teq'
  },  {
    image:'',
    title:'Fire and Shitty crap in asd teq'
  },  {
    image:'',
    title:'Fire and Shitty crap in asd teq'
  }
]

export default function Main_Page() {
  const navigate = useNavigate()

    const handleClick = () => {
        navigate( '/details',{state:{content:BookList}});
    };  

  return (
    <div className='Main_Page'>
      {/* <div className='Nav-Conta'>
        <Search/>
        <div className="Inf">
         <PersonalInfo/>
        </div>
      </div> */}

        <div style={{display:'flex'}}>
            <div className='LeftMain'>
                <Search/>
                
                <h1>Happy Reading,Jamayka</h1>
                <p>Join Us NOW and read book summarys for free , 
                    delieverd to you by experts in the field.
                    You can start your own customized journey through our help
                    to select you a wonderfull program .what are you waiting for !
                </p>

                <div style={{margin:'1rem 0'}}>
                    <Link to={"/Form_after"}>
                      <Button props={"Start your Journey"}/>
                    </Link>
                </div>

                <h1>
                Popular Now
                </h1>

                <div className="contantSearch">
                    {
                    BookList.map((item,index)=>(
                        <div className="BookSResultat" key={index} >
                        <div className="imageC" onClick={handleClick}></div>
                        <div className="title">{item.title}</div>
                        </div>
                    )) 
                    }
                </div>

                <div className='OurHelp'>
                  <div>
                    <h1>Use our help now</h1>
                    <p>We will assist you to become a better version of yourself.
                      we help you craft your own personallized journey based on
                      your Goals and likings
                    </p>
                  </div>
                  <div className="imageC" onClick={handleClick}></div>
                </div>

                <div className='OurHelp'>
                <div className="imageC" onClick={handleClick}></div>
                  <div>
                    <p>You get a 30 day plan , a book summary to read everyday carefully calibrated to make you closer to your dream.
                    </p>
                  </div>
                </div>

                <div className='OurHelp'>
                  <div>
                    <p>Each summary is carefully calibrated to help you get the most of that particulair book 
without wasting time and effort .
                    </p>
                  </div>
                  <div className="imageC" onClick={handleClick}></div>
                </div>
                      <h1 style={{marginTop:'9rem'}}>What are you waiting for section</h1>
            </div>

            <div className="RightMain">
             <PersonalInfo/>
           
            </div>
        </div>

    </div>
  )
}
