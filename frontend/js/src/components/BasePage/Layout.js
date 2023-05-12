import React, {useEffect, useState} from "react";
import Header from "../../components/Header/Header";
import {Outlet, useLocation, useResolvedPath} from "react-router-dom"
import useAuth from "../hooks/useAuth";
import Container from "@mui/material/Container";
import Box from "@mui/material/Box";

const Layout = (props) => {
    const auth = useAuth()
    // const resolver= useResolvedPath()
    const location = useLocation();
    // console.log(resolver, location)
    // console.log(props.tabs)
    // console.log(props.tabs.findIndex((p)=>{return p.link===resolver.pathname}))
    return (
        <>
            <header>
                <Header
                    auth={auth}
                    pages={props.tabs}
                    startPage={props.tabs.findIndex((p)=>{return p.link===location.pathname})}
                />

            </header>
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                <Box sx={{justifyContent: 'center'}}>

                    <Outlet context={auth}/>

                </Box>


            </Container>

            <footer> </footer>
        </>

    )
}

export {Layout}