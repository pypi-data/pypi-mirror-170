/*
 * Copyright 2020 The Kale Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import * as React from 'react';
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Grid
} from '@material-ui/core';

interface ICellMetadataEditorDialog {
  open: boolean;
  stepName: string;
  limits: { [id: string]: string };
  updateLimits: Function;
  toggleDialog: Function;
}

export const CellMetadataEditorDialog: React.FunctionComponent<ICellMetadataEditorDialog> = props => {
  const handleClose = () => {
    props.toggleDialog();
  };

  return (
    <Dialog
      open={props.open}
      onClose={handleClose}
      fullWidth={true}
      maxWidth={'sm'}
      scroll="paper"
      aria-labelledby="scroll-dialog-title"
      aria-describedby="scroll-dialog-description"
    >
      <DialogTitle id="scroll-dialog-title">
        <Grid
          container
          direction="row"
          justify="space-between"
          alignItems="center"
        >
          <Grid item xs={9}>
          </Grid>
          <Grid item xs={3}>
          </Grid>
        </Grid>
      </DialogTitle>
      <DialogContent dividers={true} style={{ paddingTop: 0 }}>
        <Grid container direction="column" justify="center" alignItems="center">
          <Grid
            container
            direction="row"
            justify="space-between"
            alignItems="center"
            style={{ marginTop: '15px' }}
          >
          </Grid>
        </Grid>
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose} color="primary">
          Ok
        </Button>
      </DialogActions>
    </Dialog>
  );
};
