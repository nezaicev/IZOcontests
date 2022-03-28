import React from "react";
import {Route, Routes, Link, BrowserRouter} from 'react-router-dom'
import VP from "../pages/VP";

const App = () => {

    return (
        <>
            <BrowserRouter>
        <Routes>
            <Route path='/frontend' element={<VP/>}/>
        </Routes>
            </BrowserRouter>
        </>


    );
}

export default App;

