% Locations database
location('Damascus').
location('Aleppo').
location('Latakia').
location('Homs').
location('Hama').
location('Tartus').
location('Daraa').
location('Deir ez-Zor').
location('Raqqa').
location('Palmyra').

mobility_mode(car).
mobility_mode(train).
mobility_mode(plane).

route_exists('Damascus','Aleppo',car).
route_exists('Damascus','Latakia',plane).
route_exists('Damascus','Homs',train).
route_exists('Damascus','Hama',car).
route_exists('Damascus','Tartus',plane).
route_exists('Damascus','Daraa',train).
route_exists('Damascus','Deir ez-Zor',plane).
route_exists('Damascus','Palmyra',train).

route_exists('Aleppo','Damascus',car).
route_exists('Aleppo','Latakia',plane).
route_exists('Aleppo','Homs',train).
route_exists('Aleppo','Hama',car).
route_exists('Aleppo','Tartus',plane).
route_exists('Aleppo','Daraa',train).
route_exists('Aleppo','Deir ez-Zor',plane).
route_exists('Aleppo','Raqqa',car).
route_exists('Aleppo','Palmyra',train).

route_exists('Latakia','Damascus',plane).
route_exists('Latakia','Aleppo',plane).
route_exists('Latakia','Homs',train).
route_exists('Latakia','Tartus',car).
route_exists('Latakia','Daraa',plane).
route_exists('Latakia','Deir ez-Zor',plane).
route_exists('Latakia','Raqqa',plane).
route_exists('Latakia','Palmyra',train).

route_exists('Homs','Damascus',train).
route_exists('Homs','Aleppo',train).
route_exists('Homs','Latakia',train).
route_exists('Homs','Hama',car).
route_exists('Homs','Tartus',train).
route_exists('Homs','Daraa',train).
route_exists('Homs','Deir ez-Zor',plane).
route_exists('Homs','Raqqa',plane).
route_exists('Homs','Palmyra',car).

route_exists('Hama','Damascus',car).
route_exists('Hama','Aleppo',car).
route_exists('Hama','Homs',car).
route_exists('Hama','Tartus',train).
route_exists('Hama','Daraa',train).
route_exists('Hama','Deir ez-Zor',plane).
route_exists('Hama','Raqqa',car).
route_exists('Hama','Palmyra',car).

route_exists('Tartus','Damascus',plane).
route_exists('Tartus','Aleppo',plane).
route_exists('Tartus','Latakia',car).
route_exists('Tartus','Homs',train).
route_exists('Tartus','Hama',train).
route_exists('Tartus','Daraa',plane).
route_exists('Tartus','Deir ez-Zor',plane).
route_exists('Tartus','Raqqa',plane).
route_exists('Tartus','Palmyra',train).

route_exists('Daraa','Damascus',train).
route_exists('Daraa','Aleppo',train).
route_exists('Daraa','Latakia',plane).
route_exists('Daraa','Homs',train).
route_exists('Daraa','Hama',train).
route_exists('Daraa','Tartus',plane).
route_exists('Daraa','Deir ez-Zor',plane).
route_exists('Daraa','Raqqa',plane).
route_exists('Daraa','Palmyra',train).

route_exists('Deir ez-Zor','Damascus',plane).
route_exists('Deir ez-Zor','Aleppo',plane).
route_exists('Deir ez-Zor','Latakia',plane).
route_exists('Deir ez-Zor','Homs',plane).
route_exists('Deir ez-Zor','Hama',plane).
route_exists('Deir ez-Zor','Tartus',plane).
route_exists('Deir ez-Zor','Daraa',plane).
route_exists('Deir ez-Zor','Raqqa',car).
route_exists('Deir ez-Zor','Palmyra',plane).

route_exists('Raqqa','Aleppo',car).
route_exists('Raqqa','Latakia',plane).
route_exists('Raqqa','Homs',plane).
route_exists('Raqqa','Hama',car).
route_exists('Raqqa','Tartus',plane).
route_exists('Raqqa','Daraa',plane).
route_exists('Raqqa','Deir ez-Zor',car).
route_exists('Raqqa','Palmyra',car).

route_exists('Palmyra','Damascus',train).
route_exists('Palmyra','Aleppo',train).
route_exists('Palmyra','Latakia',train).
route_exists('Palmyra','Homs',car).
route_exists('Palmyra','Hama',car).
route_exists('Palmyra','Tartus',train).
route_exists('Palmyra','Daraa',train).
route_exists('Palmyra','Deir ez-Zor',plane).
route_exists('Palmyra','Raqqa',car).

% Determine if a direct path is possible
path_available_direct(Start, End, Mode) :-
    route_exists(Start, End, Mode).

% Determine indirect travel path
path_available_indirect(Start, End, Paths) :-
    route_exists(Start, Intermediate, Transport1),
    path_available_direct(Intermediate, End, Transport2),
    Paths = [Transport1, Intermediate, Transport2].

% Verify travel options
travel_possible(Start, End, Paths) :-
    path_available_direct(Start, End, Paths),
    writeln('Direct route found!'),
    writeln(Paths).

travel_possible(Start, End, Paths) :-
    path_available_indirect(Start, End, Paths),
    writeln('Indirect route discovered!'),
    writeln(Paths).

% Check operation compliance
verify_operation(Operation) :-
    call(Operation), !, write('Operation verified.'), nl.
verify_operation(_) :-
    write('Operation not verified.'), nl.
