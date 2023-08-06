import { JupyterFrontEnd, JupyterFrontEndPlugin, ILayoutRestorer, ILabShell } from '@jupyterlab/application';
import { IToolbarWidgetRegistry, ReactWidget } from '@jupyterlab/apputils';
import { ITranslator } from '@jupyterlab/translation';
import { TransformerLeftPanel } from './transformerleftpanel';
import { INotebookTracker } from '@jupyterlab/notebook';
import { IDocumentManager } from '@jupyterlab/docmanager';
import { Widget } from '@lumino/widgets';
import * as React from 'react';
import '../style/index.css';

export default {
    id: 'modeldeploy-proxy-labextension:leftpanel',
    requires: [ILabShell, ILayoutRestorer, INotebookTracker, IToolbarWidgetRegistry, IDocumentManager],
    optional: [ITranslator],
    autoStart: true,
    activate: async (
        app: JupyterFrontEnd,
        labShell: ILabShell,
        restorer: ILayoutRestorer,
        tracker: INotebookTracker,
        docManager: IDocumentManager,
        toolbarRegistry: IToolbarWidgetRegistry,
        translator: ITranslator
    ): Promise<{ widget : Widget }> => {
        let widget: ReactWidget;
        async function loadPanel() {
            let reveal_widget = undefined;

            // add widget
            if (!widget.isAttached) {
                labShell.add(widget, 'left');
            }

            // open widget if resuming from a notebook
            if (reveal_widget) {
                widget.activate();
            }
        }

        app.started.then(() => {
            console.log("Leftpanel is now started...");
            widget = ReactWidget.create(
                <TransformerLeftPanel
                  app={app}
                  tracker={tracker}
                  docManager={docManager}
                />,
            );
            widget.id = 'modeldeploy-proxy-labextension/transformer-leftpanel-widget';
            widget.title.iconClass = 'transformer-logo jp-sidebar-tabicon-transformer';
            widget.title.caption = 'Transformer Panel';
            widget.node.classList.add('transformer-panel');
            restorer.add(widget, widget.id);
        });

        app.restored.then(() => {
            console.log("Leftpanel is now restored...");
            loadPanel();
        });

        return { widget };
    },
} as JupyterFrontEndPlugin<{ widget : Widget }>;
