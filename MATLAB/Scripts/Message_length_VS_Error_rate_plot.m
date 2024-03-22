% first initiate two variable in the workspace
% msglen=[];
% errrate=[];

% msglen=[64 32 16 128 128 20 25 192 18 69];
% errrate=[10.9375   6.2500   0   9.3750  9.3750  0  4.0000  7.8125  5.5556  5.7971];



msglen = [msglen,length(msg_c)];
 
 errrate = [errrate,diff/length(msg_c)*100];
 
 plot(msglen,errrate,'*b');
 xlabel("Message length");
 ylabel("Error rate (%)");