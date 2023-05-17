import Card from "@mui/material/Card";

import {Avatar, CardMedia, Chip, Paper} from "@mui/material";
import Box from "@mui/material/Box";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

import React, {useEffect} from "react";

import {ButtonDefault, DividerStyled} from "../styled";
import {host} from "../utils/consts";
import Button from "@mui/material/Button";


function CardContest(props) {
    let optionsDate = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        timezone: 'UTC',

    };

    return (

        <Card
            sx={{
                display: 'flex',
                flexWrap: 'wrap',
                marginTop: '20px',
                width: 350,
                height: '100%',

            }}>

            <CardMedia
                component="img"
                sx={{
                    width: 350,
                    display: 'block',
                    height: 'fit-content',
                }}
                image={props.data['logo']}
                alt=''
            />



            <Box sx={{
                flexWrap: "wrap",
                flexGrow: 1,
                width: 200,
                display: 'flex',
                justifyContent: 'center',

            }}>

                <CardContent>
                    <Typography variant="h6" display="block" gutterBottom>
                        {props.data['name']}
                    </Typography>
                    <Box component={'div'} sx={{marginTop: '15px'}}>

                    </Box>
                    <Box
                        dangerouslySetInnerHTML={{__html: props.data['content']}}
                        component={'div'} sx={{margin: '5px'}}>


                    </Box>
                    <DividerStyled/>
                    <Box componetn={'div'} sx={{
                        justifyContent: 'center',
                        display: 'flex',
                        marginTop: '10px'
                    }}>
                        {!props.data['hide']
                            ?
                            props.auth['id']
                                ?
                                <ButtonDefault onClick={() => {
                                    window.location.replace(`${host}/admin/`)
                                }} variant="outlined" size='small'>
                                    Принять участие
                                </ButtonDefault>
                                :
                                <ButtonDefault onClick={() => {
                                    window.location.replace(`${host}/users/login/`)
                                }} variant="outlined" size='small'>
                                    Необходима авторизация
                                </ButtonDefault>
                            : ''
                        }
                    </Box>

                </CardContent>
            </Box>


        </Card>
    )
}


export default CardContest