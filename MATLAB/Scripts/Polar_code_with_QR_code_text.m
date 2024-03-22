
s = rng(100);       % Seed the RNG for repeatability

%%
% Specify the code parameters used for a simulation. 

% Code parameters
K = 54;             % Message length in bits, including CRC, K > 30
E = 124;            % Rate matched output length, E <= 8192

EbNo = 0.8;         % EbNo in dB
L = 8;              % List length, a power of two, [1 2 4 8]
numFrames = 10;     % Number of frames to simulate
linkDir = 'DL';     % Link direction: downlink ('DL') OR uplink ('UL')

%% Polar Encoding


if strcmpi(linkDir,'DL')
    % Downlink scenario (K >= 36, including CRC bits)
    crcLen = 24;      % Number of CRC bits for DL, Section 5.1, [6]
    poly = '24C';     % CRC polynomial
    nPC = 0;          % Number of parity check bits, Section 5.3.1.2, [6]
    nMax = 9;         % Maximum value of n, for 2^n, Section 7.3.3, [6]
    iIL = true;       % Interleave input, Section 5.3.1.1, [6]
    iBIL = false;     % Interleave coded bits, Section 5.4.1.3, [6]
else
    % Uplink scenario (K > 30, including CRC bits)
    crcLen = 11;      
    poly = '11';
    nPC = 0;          
    nMax = 10;        
    iIL = false;      
    iBIL = true;      
end


%% Rate Matching and Rate Recovery


R = K/E;                          % Effective code rate
bps = 2;                          % bits per symbol, 1 for BPSK, 2 for QPSK
EsNo = EbNo + 10*log10(bps);       
snrdB = EsNo + 10*log10(R);       % in dB
noiseVar = 1./(10.^(snrdB/10)); 

% Channel
chan = comm.AWGNChannel('NoiseMethod','Variance','Variance',noiseVar);

%% Polar Decoding


% Error meter
ber = comm.ErrorRate;

%% Frame Processing Loop

numferr = 0;
%{
for i = 1:numFrames

    % Generate a random message
    msg = randi([0 1],K-crcLen,1);
    
    % Attach CRC
    msgcrc = nrCRCEncode(msg,poly);
    
    % Polar encode
    encOut = nrPolarEncode(msgcrc,E,nMax,iIL);
    N = length(encOut);
    
    % Rate match
    modIn = nrRateMatchPolar(encOut,K,E,iBIL);
    
    % Modulate
    modOut = nrSymbolModulate(modIn,'QPSK');
    
    % Add White Gaussian noise
    rSig = chan(modOut);
    
    % Soft demodulate
    rxLLR = nrSymbolDemodulate(rSig,'QPSK',noiseVar);
    
    % Rate recover
    decIn = nrRateRecoverPolar(rxLLR,K,N,iBIL);
    
    % Polar decode
    decBits = nrPolarDecode(decIn,K,E,L,nMax,iIL,crcLen); 
    
    % Compare msg and decoded bits
    errStats = ber(double(decBits(1:K-crcLen)), msg);
    numferr = numferr + any(decBits(1:K-crcLen)~=msg);

end

disp(['Block Error Rate: ' num2str(numferr/numFrames) ...
      ', Bit Error Rate: ' num2str(errStats(1)) ...
      ', at SNR = ' num2str(snrdB) ' dB'])
%}






%{


% Generate a random message
    msg = randi([0 1],K-crcLen,1);
    
    % Attach CRC
    msgcrc = nrCRCEncode(msg,poly);
    
    % Polar encode
    encOut = nrPolarEncode(msgcrc,E,nMax,iIL);
    N = length(encOut);
    
    % Rate match
    modIn = nrRateMatchPolar(encOut,K,E,iBIL);
    
    % Modulate
    modOut = nrSymbolModulate(modIn,'QPSK');
    
    % Add White Gaussian noise
    rSig = chan(modOut);
    
    % Soft demodulate
    rxLLR = nrSymbolDemodulate(rSig,'QPSK',noiseVar);
    
    % Rate recover
    decIn = nrRateRecoverPolar(rxLLR,K,N,iBIL);
    
    % Polar decode
    decBits = nrPolarDecode(decIn,K,E,L,nMax,iIL,crcLen); 
    
    rmsg=nrCRCDecode(decBits,poly);

    fprintf("\nOriginal message : %s ",num2str(msg))
    fprintf("\nReceived message : %s ",num2str(rmsg))
%}








    img=imread("C:/Users/ACER_USER/Desktop/test.jpg"); %read QR code
    [msg,~,~] = readBarcode(img);              %extract message
    msg_c = convertStringsToChars(msg);        % convert from string to char array
    msg_d = double(msg_c);                     % convert from char to integer with ASCII
    msg_bc = dec2bin(msg_d);                   % convert to binary char array
    
    
    r_bin_l=[];
    for i = 1:length(msg_bc)
        
        
        bin=zeros(23,1);    % add 23 zeros in front of each binary(in a column array binary) to reach the desired length
        
        for j = 1:7
            bin=[bin; str2num(msg_bc(i,j))]; % add the binary one by one after the 23 zeros in a column array
            
        end
        
        
    
    % Attach CRC
    msgcrc = nrCRCEncode(bin,poly);
    
    % Polar encode
    encOut = nrPolarEncode(msgcrc,E,nMax,iIL);
    N = length(encOut);
    
    % Rate match
    modIn = nrRateMatchPolar(encOut,K,E,iBIL);
    
    % Modulate
    modOut = nrSymbolModulate(modIn,'QPSK');
    
    % Add White Gaussian noise
    rSig = chan(modOut);
    
    % Soft demodulate
    rxLLR = nrSymbolDemodulate(rSig,'QPSK',noiseVar);
    
    % Rate recover
    decIn = nrRateRecoverPolar(rxLLR,K,N,iBIL);
    
    % Polar decode
    decBits = nrPolarDecode(decIn,K,E,L,nMax,iIL,crcLen); 
    
    r_bin = nrCRCDecode(decBits,poly); % received binary(in a column array)
    
    cut = r_bin(24:30)';  %trimmed binary (by removing 23 zeros in front) and flip
    
    r_bin_d = cut(1)*1000000 + cut(2)*100000 + cut(3)*10000 + cut(4)*1000 + cut(5)*100 + cut(6)*10 + cut(7); % convert to integer binary(not array binary)
    
    r_bin_c = num2str(r_bin_d); % convert to binary char array
    
    while length(r_bin_c)<7 
        r_bin_c = ['0',r_bin_c]; % add zero(s) in front to avoid uneven length of binary, if the binary starts with zero(s) and the zero(s) is cut off in the process of converting to char
    end
   
    r_bin_l = [r_bin_l; r_bin_c]; % collect the binary char arrayss into a column array(matrix)
    
    end
    
   r_dou = bin2dec(r_bin_l)'; %convert from char binary to double
   r_char = char(r_dou);      %convert from integer to char with ASCII
   r_string = convertCharsToStrings(r_char); %convert from char array to string
   

    
    fprintf("\nOriginal message : %s ",msg)
    fprintf("\nReceived message : %s \n",r_string)









rng(s);     % Restore RNG

