import React from "react";
import {Route, Routes, Link, BrowserRouter} from 'react-router-dom'
import VP from "../pages/VP";
import Artakiada from "../pages/Artakiada";

const App = () => {

    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/frontend/vp' element={<VP/>}/>
                </Routes>
                <Routes>
                    <Route path='/frontend/artakiada' element={<Artakiada/>}/>
                </Routes>
            </BrowserRouter>
        </>


    );
}

export default App;

