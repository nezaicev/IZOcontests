import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Map from "../../components/CustomIcons/Map";
import {Typography} from "@mui/material";
import Museum from "../../components/CustomIcons/Museum";
import Doctor from "../../components/CustomIcons/Doctor";
import React from "react";

const BaseInfo = () => {

    return (
        <Box sx={{
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            alignItems: 'center'
        }}>

            <Button onClick={() => {
                window.location.href = 'http://konkurs.shkola-nemenskogo.ru/map/'
            }}>
                <Box sx={{margin: '10px'}}>
                    <Map sx={{fontSize: 70}}/>
                    <Typography sx={{color: "#212121"}} variant="button" display="block"
                                gutterBottom>
                        Проект «Мой любимый край»
                    </Typography>
                </Box>

            </Button>
            <Button onClick={() => {
                window.location.href = 'http://cnho.ru/?page_id=15392'
            }}>
                <Box sx={{margin: '10px'}}>
                    <Museum sx={{fontSize: 70}}/>
                    <Typography sx={{color: "#212121"}} variant="button" display="block"
                                gutterBottom>
                        АРТ-КВЕСТЫ «Путешествие по виртуальным музеям
                    </Typography>
                </Box>

            </Button>
            <Button onClick={() => {
                window.location.href = 'http://cnho.ru/?page_id=15869'
            }}>
                <Box sx={{margin: '10px'}}>
                    <Doctor sx={{fontSize: 70}}/>
                    <Typography sx={{color: "#212121"}} variant="button" display="block"
                                gutterBottom>
                        #СПАСИБО ВРАЧАМ!
                    </Typography>
                </Box>

            </Button>

        </Box>


    )
}

export {BaseInfo}