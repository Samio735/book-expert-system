import React ,{useState} from 'react'
import "./Search.css"
import searchIcon from '../scenes/images/icons8-search-100 2.png';

export default function Search() {
    const [searchText, setSearchText] = useState("");

    const handleSearch = (event) => {
      setSearchText(event.target.value);
    };
  
  return (
    <>
    <div className="search-bar">
        <img src={searchIcon} alt="Search Icon" />
        <input
            type="text"
            placeholder="Search Book Summary ...."
            value={searchText}
            onChange={handleSearch}
        />
    </div>
    </>
  )
}
