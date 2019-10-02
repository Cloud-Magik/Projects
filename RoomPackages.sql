create table RoomPackages(
    Bedroom_type text not null,  
	Beds text not null,
    Amenities text not null,
    Price text not null
)

insert into RoomPackages(Bedroom_type, Beds, Amenities, Price)
values ('homeless_deluxe', 'makeshift_bed', 'Lights_turned_on', '$50' ),
('Single', 'Single_bed', 'color_tv', '$75' ),
('Couple', 'Two_beds', 'Intimate_accessories', '$100'),
('Queen', 'Queen_bed', 'manservant', '$150'),
('King', 'King_bed', 'Everything_a_king_wants', '$300'),
('Presidential', 'Two_King_beds', 'Presidential_rights', '$500'),
('RICH_AF', 'Personal_cloud_bed', 'ownership_of_world(for_time_period)', '$1000')


select * from RoomPackages

delete from RoomPackages

update RoomPackages

