/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Server;

import cFramework.nodes.area.Area;
import conf.Names;

/**
 *
 * @author arman
 */
public class Server extends Area {
    
    public Server(){
        this.ID = Names.Server;
        this.namer = Names.class;
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
        log.message(new String(data));
    }
    
}