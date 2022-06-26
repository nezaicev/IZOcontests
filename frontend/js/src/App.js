import './App.css';
import React from "react";
import {Route, Routes, Link, BrowserRouter} from 'react-router-dom'
import GalleryPageVP from "./pages/VP/GalleryPageVP";
import GalleryPageArtakiada from "./pages/ARTAKIADA/GalleryPageArtakiada";
import GallaryPageNRusheva from "./pages/NRUSHEVA/GallaryPageNRusheva";
import GalleryPageMyMoskvichi
    from "./pages/MYMOSKVICHI/GalleryPageMyMoskvichi";


const App = () => {

    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/frontend/vp/' element={<GalleryPageVP/>}/>
                    <Route path='/frontend/artakiada/' element={<GalleryPageArtakiada/>}/>
                    <Route path='/frontend/nrusheva/' element={<GallaryPageNRusheva/>}/>
                    <Route path='/frontend/mymoskvichi/' element={<GalleryPageMyMoskvichi/>}/>
                </Routes>

            </BrowserRouter>
        </>


    );
}
export default App