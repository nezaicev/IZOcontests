import Box from "@mui/material/Box";
import {Chip, CircularProgress, Paper, Typography} from "@mui/material";
import LocationOnIcon from '@mui/icons-material/LocationOn';
import React, {useEffect, useState} from "react";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {optionsSRLWrapper} from "../../components/styled";
import ImageListItem from "@mui/material/ImageListItem";
import Card from "@mui/material/Card";
import {createLabel} from "../../components/utils/utils";
import Header from "../../components/Header/Header";
import {host} from "../../components/utils/consts";
import Container from "@mui/material/Container";
import {useParams} from "react-router-dom";
import useAuth from "../../components/hooks/useAuth";
import dataFetch from "../../components/utils/dataFetch";



function BasePage(props) {
    const auth = useAuth()
    const [fetchAll, setFetchAll] = useState(false);
    const [value, setValue] = React.useState(0);
    const [data, setData] = React.useState({})


    let {slug} = useParams()
    let pages = [
    {'name': data.title , 'link': `/frontend/api/page/${slug}/`},

]


    useEffect(() => {
        dataFetch(`${host}/frontend/api/page/${slug}/`, null, (data) => {
            setData(data);
            setFetchAll(true)
        })
    }, [])


    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header
                    pages={pages}
                    activePage={(newValue) => (setValue(newValue))}
                    auth={auth}
                    // mainLink={`${host}/frontend/expositions/`}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                {fetchAll ? <Box>
                    <Box sx={{
                        justifyContent: 'center',
                        display: 'flex',
                        marginTop: '30px',
                        marginBottom: '20px'
                    }}>
                        <Typography variant="h5">
                            {data.subtitle}
                        </Typography>
                    </Box>


                    <Paper

                        dangerouslySetInnerHTML={{__html: data.content}}
                        scroll={'body'}
                        sx={{
                            boxShadow: 0,
                            // maxHeight: 600,
                            overflow: 'auto',
                            padding: ['5px', '15px'],
                        }}

                    />


                </Box> : <Box sx={{
                    justifyContent: 'center',
                    height: '600',
                    display: 'flex',
                    marginTop: ' 20px'
                }}>
                    <CircularProgress sx={{
                        color: '#d26666'
                    }}/>
                </Box>
                }


            </Container>
        </Box>


    )
}

export default BasePage

