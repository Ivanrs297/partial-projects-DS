/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area3;

import Area1.*;
import conf.Names;

/**
 *
 * @author arman
 */
public class Process3 extends cFramework.nodes.process.Process {
    
    public Process3 () {
        this.ID = Names.Process3;
        this.namer = Names.class;
    }

    @Override
    public void receive(long nodeID, byte[] data) {
        log.message("Recibido Proceso 3");
        log.message(""+ this.currentMetadata.time );
        send(Names.Process4, data);
    }
    
}
