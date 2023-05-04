import Box from "@mui/material/Box";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import React, {useEffect, useState} from "react";
import useAuth from "../../components/hooks/useAuth";
import {CircularProgress, Grid} from "@mui/material";
import CardEvent from "../../components/Event/CardEvent";
import StatContestTable from "../../components/Statistics/StatContestTable";
import dataFetch from "../../components/utils/dataFetch";
import StatEventTable from "../../components/Statistics/StatEventTable";
import {DividerStyled} from "../../components/styled";


let pages = [
    {'name': 'Статистика', 'link': '/frontend/api/statistics/'},
]

const host = process.env.REACT_APP_HOST_NAME



function ContestsStatistics() {

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

                <Box>

                    {function () {
                        if (fetchAll) {
                            return (
                                <Box>
                                    <Box>
                                        <StatContestTable data={data.contests}/>
                                    </Box>
                                <DividerStyled sx={{marginTop:'15px', marginBottom:'15px'}}/>
                                    <Box>
                                        <StatEventTable data={data.events}/>
                                    </Box>

                                </Box>

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



    )

}

export {ContestsStatistics}