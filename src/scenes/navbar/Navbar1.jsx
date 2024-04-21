import React,{useState} from 'react'
import { Link } from 'react-router-dom';
import homeIcon from "../images/icons8-smart-home-96 (1) 1.png"
import searchIcon from "../images/icons8-search-100 2.png"
import saveIcon from "../images/icons8-bookmark-100 1.png"
import imageIcon from "../images/icons8-adventure-100 1.png"
import "./navbar.css"

export default function Navbar1() {

  const [activeIcon, setActiveIcon] = useState('home');
  const handleIconClick = (iconName) => {
      setActiveIcon(iconName);
  };

  return (
    <div className="navbar">
      <p>AW</p>
      <Link to="/" onClick={() => handleIconClick('home')}>
        <img src={homeIcon} alt="Home" className={activeIcon === 'home' ? 'active' : ''} />
      </Link>
      <Link to="/Search" onClick={() => handleIconClick('search')}>
        <img src={searchIcon} alt="Search" className={activeIcon === 'search' ? 'active' : ''} />
      </Link>
      <Link to="/Journey" onClick={() => handleIconClick('image')}>
        <img src={imageIcon} alt="" className={activeIcon === 'image' ? 'active' : ''} />
      </Link>
      <Link to="/" onClick={() => handleIconClick('save')}>
        <img src={saveIcon} alt="Save" className={activeIcon === 'save' ? 'active' : ''} />
      </Link>
    </div>
  )
}
