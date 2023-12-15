import React, {useEffect, useState} from "react";
import dataFetch from "../../components/utils/dataFetch";
import {getExcludeData} from "../../components/utils/utils";
import {Box} from "@mui/material";
import HorizontalTabs from "../../components/Gallary/HorizontalTabs";
import VerticalTabs from "../../components/Gallary/VerticalTabs";
import VisibleBoxImages from "../../components/Gallary/VisibleBoxImages";



const excludeYears = []
const contestName=process.env.REACT_APP_IZO_DICTANT


function GalleryPageIzoDictant(props) {
    const [dataHorizontalTabs, setDataHorizontalTabs] = React.useState([])
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const [params, setParams] = React.useState({contest_name: contestName})
    const [page, setPage] = useState(1)


    useEffect(() => {

        dataFetch(props.urlHorizontalTabs, params, (data) => {
            setDataHorizontalTabs(data, [setValueHorizontalTabs(0)])
            setPage(1)
        })
    }, [])

    useEffect(() => {
        params['year_contest'] = dataHorizontalTabs[valueHorizontalTabs]


    }, [dataHorizontalTabs, valueHorizontalTabs])


    return (<React.Fragment>
            <Box sx={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                alignItems: 'center'
            }}>

                <HorizontalTabs contestName={contestName}
                                data={dataHorizontalTabs}
                                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue), [setPage(1)]))}

                />


            </Box>

            {/*<CreativeTack data={valueCreativeTack}/>*/}

            <Box sx={{}}>

                <VisibleBoxImages
                    url={props.urlContent}
                    contestName={contestName}
                    year={dataHorizontalTabs[valueHorizontalTabs]}
                    page={page}
                    ordering={'rating'}
                    setPage={(newValue) => {
                        setPage(newValue)
                    }}
                />

            </Box>
        </React.Fragment>
    )
}



export {GalleryPageIzoDictant}