import './App.css';
import React from "react";
import {Router, Route, Routes, Switch, Link, BrowserRouter} from 'react-router-dom'
import GalleryPageVP from "./pages/VP/GalleryPageVP";
import GalleryPageArtakiada from "./pages/ARTAKIADA/GalleryPageArtakiada";
import GallaryPageNRusheva from "./pages/NRUSHEVA/GallaryPageNRusheva";
import GalleryPageMyMoskvichi
    from "./pages/MYMOSKVICHI/GalleryPageMyMoskvichi";
import MainPage from "./pages/MAIN/MainPage";
import EventPage from "./pages/EVENT/EventPage";
import BroadcastListPage from "./pages/BROADCAST/BroadcastListPage";
import BroadcastPage from "./pages/BROADCAST/BroadcastPage";




const App = () => {
        console.log('test')
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route path='/frontend/main/' element={<MainPage/>}/>
                    <Route path='/frontend/vp/' element={<GalleryPageVP/>}/>
                    <Route path='/frontend/artakiada/' element={<GalleryPageArtakiada/>}/>
                    <Route path='/frontend/nrusheva/' element={<GallaryPageNRusheva/>}/>
                    <Route path='/frontend/mymoskvichi/' element={<GalleryPageMyMoskvichi/>}/>
                    <Route path='/frontend/event/:id/' element={<EventPage/>} />
                    <Route path='/frontend/broadcasts/' element={<BroadcastListPage/>} />
                    <Route path='/frontend/broadcast/:id/' element={<BroadcastPage/>} />

                </Routes>
                {/*<Switch>*/}
                {/*     <Route path='/frontend/event/:id/' children={<EventPage/>} />*/}
                {/*</Switch>*/}

            </BrowserRouter>

        </>


    );
}
export default App