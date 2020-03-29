package testmiddlewarepython;


import cFramework.nodes.service.Igniter;
//@import


/*
https://www.enmimaquinafunciona.com/pregunta/90466/como-clonar-git-repositorio-solo-algunos-directorios
*/

public class Init extends Igniter {
    
    public Init() {
        
        String[] areaNames = {
            TestArea.class.getName()
        };

        configuration.setLocal(true);
        configuration.setDebug(null);
        configuration.setTCP();
        setAreas(areaNames);
    
        run();
    }

    public static void main(String[] args) {
        new Init();
    }
}
