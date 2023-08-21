import VerticalTabs from "../VerticalTabs";
import HorizontalTabs from "../HorizontalTabs";
import React, {useEffect, useState} from "react";
import {Box} from "@mui/material";
import dataFetch from "../../utils/dataFetch";
import VisibleBoxImages from "../VisibleBoxImages";
import CreativeTack from "../CreativeTack";
import {getExcludeData} from "../../utils/utils";

const excludeYears=['2023-2024 год']


export default function GalleryArtakiada(props) {
    const [dataVerticalTabs, setDataVerticalTabs] = React.useState([])
    const [valueVerticalTabs, setValueVerticalTabs] = React.useState('')
    const [dataHorizontalTabs, setDataHorizontalTabs] = React.useState([])
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const [valueCreativeTack, setValueCreativeTack] = React.useState('')
    const [params, setParams] = React.useState({contest_name: props.contestName})
    const [page, setPage] = useState(1)


    useEffect(() => {
        dataFetch(props.urlVerticalTabs, params, (data) => {
            setDataVerticalTabs(getExcludeData(data, excludeYears), [setValueVerticalTabs(0)]);
        })
    }, [])

    useEffect(() => {
        params['year_contest'] = dataVerticalTabs[valueVerticalTabs]
        dataFetch(props.urlHorizontalTabs, params, (data) => {
            setDataHorizontalTabs(data, [setValueHorizontalTabs(0)])
            setPage(1)
        })
    }, [valueVerticalTabs])

    useEffect(() => {
        params['year_contest'] = dataVerticalTabs[valueVerticalTabs]
        params['theme'] = dataHorizontalTabs[valueHorizontalTabs]
        dataFetch(props.urlCreativeTack, params, (data) => {
            setValueCreativeTack(data)
        })
    }, [dataHorizontalTabs, valueHorizontalTabs])

    return (<React.Fragment>
            <Box sx={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                alignItems: 'center'
            }}>

                <HorizontalTabs contestName={props.contestName}
                                data={dataHorizontalTabs}
                                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue), [setPage(1)]))}
                                valueVerticalTabs={valueVerticalTabs}
                />

                <VerticalTabs contestName={props.contestName}
                              data={dataVerticalTabs}
                              setValueVerticalTabs={(newValue) => (setValueVerticalTabs(newValue, [setPage(1)]))}

                />
            </Box>

            <CreativeTack data={valueCreativeTack}/>

            <Box sx={{}}>

                <VisibleBoxImages
                    url={props.urlContent}
                    contestName={props.contestName}
                    year={dataVerticalTabs[valueVerticalTabs]}
                    theme={dataHorizontalTabs[valueHorizontalTabs]}
                    page={page}
                    setPage={(newValue) => {
                        setPage(newValue)
                    }}
                />

            </Box>
        </React.Fragment>
    )
}