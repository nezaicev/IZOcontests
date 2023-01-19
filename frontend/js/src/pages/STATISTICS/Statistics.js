import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import React, {useEffect, useState} from "react";
import useAuth from "../../components/hooks/useAuth";
import {CircularProgress, Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import StatContestTable from "../../components/Statistics/StatContestTable";
import dataFetch from "../../components/utils/dataFetch";


let pages = [
    {'name': 'Статистика', 'link': '/frontend/api/statistics/'},
]

const host = process.env.REACT_APP_HOST_NAME

function Statistics() {

    const auth = useAuth()
    const [fetchAll, setFetchAll] = useState(false);
    const [data, setData] = React.useState([])
    const [value, setValue] = React.useState(0);


      useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
            setData(data);
            setFetchAll(true)
        })
    }, [])


    useEffect(() => {
        dataFetch(`${host}${pages[value]['link']}`, null, (data) => {
            setData(data);
        })
    }, [value])

    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header pages={pages}
                    activePage={(newValue) => (setValue(newValue))}
                    auth={auth}
                    mainLink={`${host}/frontend/main/`}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center',
            }}>
                <Box>

                    {function () {
                        if (fetchAll) {
                            return (
                                <StatContestTable data={data}/>

                            )
                        } else {
                            return (
                                <Box sx={{
                                    justifyContent: 'center',
                                    height: '600',
                                    display: 'flex',
                                    marginTop: ' 20px'
                                }}>
                                    <CircularProgress sx={{
                                        color: '#d26666'
                                    }}/>
                                </Box>)
                        }
                    }()

                    }

                </Box>


            </Container>
        </Box>

    )

}

export default Statistics