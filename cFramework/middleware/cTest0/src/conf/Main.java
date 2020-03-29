/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package conf;

import cFramework.nodes.service.Igniter;

/**
 *
 * @author arman
 */
public class Main extends Igniter{
    
    public Main(){
        String[] areaNames = {
            Area1.Area1.class.getName(),
            Area2.Area2.class.getName(),
        };
        setAreas(areaNames);
        configuration.setDebug(null);
        configuration.setLocal(false);
        run();
    }
    
    
    public static void main(String[] arg){
        
        new Main();
    }
}
