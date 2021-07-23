import logo from './logo.svg';
import './App.css';
import {useEffect,useState} from "react";
import axios from "axios";
import PostList from "./Components/posts-list";

const url="http://127.0.0.1:8000/api/posts/"

function App() {
  const [posts,setState] = useState([]);

  useEffect(()=>{
    axios.get(url)
    .then(res=>{
      console.log(res);
      console.log(res.data);
    })
    .catch((err)=>console.log(err))

  },[])
  return (
    <div className="App">
      <h5>First React Project</h5>
      <hr />
      <PostList />
    </div>
  );
}

export default App;
