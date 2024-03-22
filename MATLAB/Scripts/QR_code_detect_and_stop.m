function[]=test()
cam=webcam('vga');
msg="";
dF="";
n=0;

while msg=='' & dF==''    
     
    img=snapshot(cam); 
    
    [msg,dF,loc]=readBarcode(img);
    
    
    if msg=='' & dF==''
        fprintf('\n%d  No QR code detected\n\n',n);
        img=insertText(img,[0,480],' No QR code detected','AnchorPoint','LeftBottom','BoxOpacity',1,'FontSize',25);
        % insertText extra arguments : Font, FontSize, TextColor, BoxColor, BoxOpacity, AnchorPoint
        
        
    elseif msg~='' & dF~=''
        fprintf('%d  QR code detected : %s\n\n',n,msg);
        img=insertText(img,[loc(1,1)-20,loc(1,2)+30],msg,'BoxOpacity',1,'FontSize',12);
        img=insertShape(img,'FilledCircle',[loc,repmat(5,length(loc),1)],'Color','red','Opacity',1);
        % insertShape arguments : img,shape,position,'LineWidth','Color','Opacity','SmoothEdges'
        % shape : Rectangle,FilledRectangle,Line,Polygon,FilledPolygon,Circle,FilledCircle
        % repmat(5,3,1) = [5;5;5] 
    end
    
    n=n+1;
    imshow(img);
    
    end    
%clear('cam');
end
