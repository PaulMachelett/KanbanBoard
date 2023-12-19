import './App.css';
import * as React from 'react';
import SignIn from './pages/SignIn';
import {Home} from './pages/Home'
import { Project } from './pages/Project';
import { Route, Routes,BrowserRouter } from "react-router-dom";
import About from "./pages/About"
function App() {
  return (
  <BrowserRouter>
 <Routes>
    <Route path="/signIn" element={<SignIn/>}/>
    <Route path="/" element = {<Home/>}/>
    <Route path="/about" element = {<About/>}/>
    <Route path='/project' element = {<Project/>}/>
      
 </Routes>
 </BrowserRouter>
   
 );
}

export default App;
