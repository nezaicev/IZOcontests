import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {getFormattedDate} from "../utils/utils";

  let optionsDate = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    };



export default function StatEventTable(props) {

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell>Мероприятие</TableCell>
            <TableCell align="center">Дата</TableCell>
            <TableCell align="right">Заявки</TableCell>
            <TableCell align="right">Обр. организации</TableCell>
            <TableCell align="right">Регионы</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {props.data.map((row) => (
            <TableRow
              key={row.name_event}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name_event}
              </TableCell>
              <TableCell align="right">{getFormattedDate(row.date_event, optionsDate)}</TableCell>
              <TableCell align="right">{row.participant_count}</TableCell>
              <TableCell align="right">{row.school_count}</TableCell>
              <TableCell align="right">{row.region_count}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}